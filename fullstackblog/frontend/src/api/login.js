import fetch from 'utils/fetch'

export function loginByUsername(username, password) {
  const data = {
    username,
    password
  }
  return fetch({
    url: 'http://127.0.0.1:8000/rest-auth/login/',
    method: 'post',
    data
  })
}

export function getInfo() {
  return fetch({
    url: 'http://127.0.0.1:8000/rest-auth/user/',
    method: 'get',
  })
}

export function logout() {
  return fetch({
    url: 'http://127.0.0.1:8000/rest-auth/logout/',
    method: 'post'
  })
}