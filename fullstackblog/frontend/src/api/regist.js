import fetch from 'utils/fetch'

export function registUser(data) {
  return fetch({
    url: 'http://127.0.0.1:8000/rest-auth/registration/',
    method: 'post',
    data
  })
}