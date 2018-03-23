package main

import (
	"log"
	"net/http"

	"github.com/gorilla/websocket"
)

type room struct {
	//forward는 수신 메시지를 보관하는 채널이며
	//수신한 메세지는 다른 클라이언트로 전달돼야한다
	forward chan []byte

	//join은 방에 들어오려는 클라이언트를 위한 채널이다
	join chan *client

	//leave는 방을 나가길 원하는 클라이언트를 위한 채널이다
	leave chan *client

	//clients는 현재 채팅방에 있는 모든 클라이언트를 보유한다
	clients map[*client]bool
}

func (r *room) run() {
	for {
		select {
		case client := <-r.join:
			//입장
			r.clients[client] = true
		case client := <-r.leave:
			//퇴장
			//delete(map, keyValue)
			delete(r.clients, client)
			//clse(chanel)
			close(client.send)
		case msg := <-r.forward:
			//모든 클라이언트에 메세지를 전달
			for client := range r.clients {
				client.send <- msg
			}
		}
	}
}

const (
	socketBuffersSize  = 1024
	messageBuffersSize = 256
)

var upgrader = &websocket.Upgrader{ReadBufferSize: socketBuffersSize,
	WriteBufferSize: socketBuffersSize}

func (r *room) ServeHTTP(w http.ResponseWriter, req *http.Request) {
	socket, err := upgrader.Upgrade(w, req, nil)
	if err != nil {
		log.Fatal("ServeHTTP :", err)
		return
	}

	client := &client{
		socket: socket,
		send:   make(chan []byte, messageBuffersSize),
		room:   r,
	}

	r.join <- client
	defer func() { r.leave <- client }()
	go client.write()
	client.read()
}

func newRoom() *room {
	return &room{
		forward: make(chan []byte),
		join:    make(chan *client),
		leave:   make(chan *client),
		clients: make(map[*client]bool),
	}
}
