import { createAsyncThunk } from '@reduxjs/toolkit'
import { IServiceType } from '@/models/service-type/index.types'
import { fetchCore } from '@/shared/libs'
import { toastError } from '@/shared/utils'

export const fetchServiceTypes = createAsyncThunk<IServiceType[]>(
	'service-types/all',
	async (_, thunkApi) => {
		try {
			const response = await fetchCore({
				url: 'v1/service-types/',
			})
			return (await response.json()) as IServiceType[]
		} catch (e) {
			toastError(e)
			return thunkApi.rejectWithValue('Error fetching service types')
		}
	},
)
