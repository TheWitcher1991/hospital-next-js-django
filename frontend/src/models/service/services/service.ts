import { createApi } from '@reduxjs/toolkit/query/react'
import { fetchCoreQuery } from '@/shared/libs'
import { IService } from '@/models/service/types/service'

export const ServiceApi = createApi({
	reducerPath: 'serviceApi',
	baseQuery: fetchCoreQuery({
		base_url: 'v1/services/',
		isAuthorized: false,
	}),
	tagTypes: ['services'],
	endpoints: (build) => ({
		getServices: build.query<IService[]>({
			query: () => '',
			providesTags: ['services'],
		}),
	}),
})

export const { useGetServicesQuery } = ServiceApi
