import { createApi } from '@reduxjs/toolkit/query'
import { fetchCoreQuery } from '@/libs'
import { ILogin, ILoginReturn } from '@/models/auth'

export const AuthService = createApi({
	reducerPath: 'auth',
	baseQuery: fetchCoreQuery(),
	endpoints: (builder) => ({
		login: builder.mutation<ILoginReturn, ILogin>({
			query: (data) => ({
				url: 'login/',
				method: 'POST',
				body: data,
			}),
		}),
	}),
})

export const { useLoginMutation } = AuthService
