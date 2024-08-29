import { createApi } from '@reduxjs/toolkit/query/react'
import { fetchCoreQuery } from '@/shared/libs'
import { IService } from '@/models/service/index.types'

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
		getServiceById: build.query<IService, number>({
			query: (id) => `${id}/`,
			providesTags: (result, error, { id }) => [{ type: 'services', id }],
		}),
	}),
})

export const { useGetServicesQuery, useGetServiceByIdQuery } = ServiceApi
