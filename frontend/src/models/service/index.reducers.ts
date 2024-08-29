import { ServiceState } from '@/models/service/index.types'
import { createSlice, PayloadAction } from '@reduxjs/toolkit'
import { stringIncludes } from '@/shared/utils'

const initialState: ServiceState = {
	count: 0,
	services: [],
}

export const serviceSlice = createSlice({
	name: 'service',
	initialState,
	reducers: {
		setCount: (state, action: PayloadAction<number>) => {
			state.count = action.payload
		},
		setServices: (
			state,
			action: PayloadAction<ServiceState['services']>,
		) => {
			state.services = action.payload
		},
		filterServices: (state, action: PayloadAction<string>) => {
			state.services = state.services.filter((s) =>
				stringIncludes(s.name, action.payload),
			)
		},
	},
})

export const serviceReducer = serviceSlice.reducer
export const serviceSelectors = serviceSlice.selectors
export const serviceActions = serviceSlice.actions
