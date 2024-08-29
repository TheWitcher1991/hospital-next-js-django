import { fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import { RootState } from '@/store'

export const BASE_URL = 'http://localhost:8000/api/'

type fetchCoreQueryOptions = {
	base_url?: string
	credentials?: RequestCredentials
	token_type?: string
	isAuthorized?: boolean
}

export const fetchCoreQuery = ({
	base_url = '',
	credentials = 'include',
	token_type = 'Bearer',
	isAuthorized = true,
}: fetchCoreQueryOptions) => {
	return fetchBaseQuery({
		baseUrl: `${BASE_URL}${base_url}`,
		prepareHeaders: (headers, { getState }) => {
			if (isAuthorized) {
				const token = (getState() as RootState).account?.access_token
				if (token) {
					headers.set('authorization', `${token_type} ${token}`)
				}
			}
			headers.set('content-type', 'application/json')
			headers.set('accept', 'application/json')
			return headers
		},
		credentials: credentials,
	})
}
