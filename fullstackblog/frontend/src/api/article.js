import fetch from 'utils/fetch'

export function getList() {
  return fetch({
    url: 'http://127.0.0.1:8000/api/post/',
    method: 'get'
  })
}