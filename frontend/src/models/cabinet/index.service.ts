import { createApi } from '@reduxjs/toolkit/query/react'
import { fetchCoreQuery } from '@/shared/libs'

export const CabinetApi = createApi({
	reducerPath: 'cabinetApi',
	baseQuery: fetchCoreQuery({
		isAuthorized: false,
	}),
	endpoints: build => ({}),
})

export const {} = CabinetApi
