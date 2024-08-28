import { createApi } from '@reduxjs/toolkit/query/react'
import { ILogin, ILoginReturn } from '@/models/auth/index.types'
import { fetchCoreQuery } from '@/shared/libs'

export const AuthService = createApi({
	reducerPath: 'authApi',
	baseQuery: fetchCoreQuery({}),
	endpoints: (builder) => ({
		login: builder.mutation<ILoginReturn, ILogin>({
			query: (data) => ({
				url: 'login/',
				method: 'POST',
				body: data,
			}),
		}),
		logout: builder.mutation({
			query: () => ({
				url: 'logout/',
				method: 'POST',
			}),
		}),
	}),
})

export const { useLogoutMutation, useLoginMutation } = AuthService
