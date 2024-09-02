import { createApi } from '@reduxjs/toolkit/query/react'
import { fetchCoreQuery } from '@/shared/libs'

export const ScheduleApi = createApi({
	reducerPath: 'scheduleApi',
	baseQuery: fetchCoreQuery({
		isAuthorized: true,
	}),
	endpoints: build => ({}),
})

export const {} = ScheduleApi
