import { createApi } from '@reduxjs/toolkit/query/react'
import { fetchCoreQuery } from '@/shared/libs'

export const TalonApi = createApi({
	reducerPath: 'talonApi',
	baseQuery: fetchCoreQuery({
		isAuthorized: true,
	}),
	endpoints: build => ({}),
})

export const {} = TalonApi
