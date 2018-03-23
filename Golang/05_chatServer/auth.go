package main

import (
	"github.com/stretchr/gomniauth"
	"fmt"
	"log"
	"net/http"
	"strings"
)

type authHandler struct {
	next http.Handler
}

func (h *authHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	_, err := r.Cookie("auth")
	if err == http.ErrNoCookie {
		//인증불가
		w.Header().Set("Location", "/Login")
		w.WriteHeader(http.StatusTemporaryRedirect)
		return
	}
	if err != nil {
		//다른에러
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	//성공 다음 핸들러 호출
	h.next.ServeHTTP(w, r)
}

func MustAuth(handler http.Handler) http.Handler {
	return &authHandler{next: handler}
}

//loginHandler는 서드파티 로그인 프로세스를 처리한다
//형식: /auth/{action}/{provider}
func loginHandler(w http.ResponseWriter, r *http.Request) {
	segs := strings.Split(r.URL.Path, "/")
	action := segs[2]
	provider := segs[3]
	switch action {
	case "login":
		provider, err := gomniauth.Provider(provider)
		if err != nil{
			http.Error(w, fmt.Sprintf("Error when trying to get provider %s: %s",
				provider,err), http.StatusBadRequest)
			return
		}
		loginUrl, err := provider.GetBeginAuthURL(nil, nil)
		if err != nil{
			http.Error(w, fmt.Sprintf("Error when trying to get GetBeginAuthURL for %s: %s",
				provider,err), http.StatusInternalServerError)
			return
		}
		w.Header().Set("Location", loginUrl)
		w.WriteHeader(http.StatusTemporaryRedirect)
	default:
		w.WriteHeader(http.StatusNotFound)
		fmt.Fprintf(w, "Auth action %s not supported", action)
	}
}

http://localhost:8080/auth/login/facebook