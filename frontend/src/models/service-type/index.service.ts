import { createApi } from '@reduxjs/toolkit/query/react'
import { fetchCore, fetchCoreQuery } from '@/shared/libs'
import { IServiceType } from '@/models/service-type/index.types'
import { createAsyncThunk } from '@reduxjs/toolkit'

export const ServiceTypeApi = createApi({
	reducerPath: 'serviceTypeApi',
	baseQuery: fetchCoreQuery({
		base_url: 'v1/service-types/',
		isAuthorized: false,
	}),
	tagTypes: ['service-types'],
	endpoints: (build) => ({
		getServiceTypes: build.query<IServiceType[]>({
			query: () => '',
			providesTags: ['service-types'],
		}),
		getServiceTypeById: build.query<IServiceType, number>({
			query: (id) => `${id}/`,
			providesTags: (result, error, { id }) => [
				{ type: 'service-types', id },
			],
		}),
	}),
})

export const fetchServiceTypes = createAsyncThunk<IServiceType[]>(
	'service-types/all',
	async (_, thunkApi) => {
		try {
			const response = await fetchCore({
				url: 'v1/service-types/',
			})
			return (await response.json()) as IServiceType[]
		} catch (e) {
			return thunkApi.rejectWithValue('Error fetching service types')
		}
	},
)

export const { useGetServiceTypesQuery, useGetServiceTypeByIdQuery } =
	ServiceTypeApi
