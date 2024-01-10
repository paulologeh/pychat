import { fetcher } from 'utils'

const ROOT_URL = `${process.env.REACT_API_URL}/api/search`

export class Search {
  static searchAll(term: string) {
    return fetcher(`${ROOT_URL}?term=${term}`, 'GET')
  }

  static searchUser(username: string) {
    return fetcher(`${ROOT_URL}/user/${username}`, 'GET')
  }
}
