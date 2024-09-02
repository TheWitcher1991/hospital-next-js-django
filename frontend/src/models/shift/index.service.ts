import { createApi } from '@reduxjs/toolkit/query/react'
import { fetchCoreQuery } from '@/shared/libs'

export const ShiftApi = createApi({
	reducerPath: 'shiftApi',
	baseQuery: fetchCoreQuery({
		isAuthorized: false,
	}),
	endpoints: build => ({}),
})

export const {} = ShiftApi
