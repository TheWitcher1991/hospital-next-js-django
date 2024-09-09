import { fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import store, { RootState } from '@/store'

export const BASE_URL = 'http://localhost:8000/api/'

type fetchCoreQueryOptions = {
	base_url?: string
	credentials?: RequestCredentials
	token_type?: string
	mode?: RequestMode
	cache?: RequestCache
	isAuthorized?: boolean
}

export const fetchCoreQuery = ({
	base_url = '',
	credentials = 'include',
	token_type = 'Bearer',
	mode = 'cors',
	cache = 'no-cache',
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
		mode: mode,
		cache: cache,
		credentials: credentials,
	})
}

type fetchCoreOptions = {
	url: string
	method?: 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE'
	token_type?: string
	headers?: HeadersInit
	body?: any
	cache?: RequestCache
	credentials?: RequestCredentials
	isAuthorized?: boolean
}

export const fetchCore = async ({
	url = '',
	method = 'GET',
	token_type = 'Bearer',
	body = {},
	mode = 'cors',
	cache = 'default',
	credentials = 'include',
	headers = {},
	isAuthorized = true,
}: fetchCoreOptions) => {
	return await fetch(`${BASE_URL}${url}`, {
		method: method as string,
		headers: {
			'Content-Type': 'application/json',
			Accept: 'application/json',
			...(isAuthorized && {
				Authorization: `${token_type} ${store.getState().account?.access_token}`,
			}),
			...headers,
		},
		body: JSON.stringify(body),
		mode: mode,
		cache: cache,
		credentials: credentials,
	})
}
