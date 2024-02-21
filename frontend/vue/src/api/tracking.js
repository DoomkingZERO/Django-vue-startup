import request from '@/utils/request'

export function pingTracking(user) {
    return request({
        url: `v1/tracking/${user}`,
        method: 'post',
        cache: false
    })
}

export function listUsers(page, query) {
  const params = {};
  if (query) {
    params.search = query;
  }
  return request({
    url: `/v1/users/`,
    method: 'get',
    params,
    cache: false
  })
}
