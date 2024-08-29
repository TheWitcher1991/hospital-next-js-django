import { createSlice, PayloadAction } from '@reduxjs/toolkit'
import { ServiceTypeState } from '@/models/service-type/index.types'
import { fetchServiceTypes } from '@/models/service-type/index.service'
import { stringIncludes } from '@/shared/utils'

const initialState: ServiceTypeState = {
	count: 0,
	isLoading: false,
	isError: false,
	types: [],
}

export const serviceTypeSlice = createSlice({
	name: 'service-type',
	initialState,
	reducers: {
		setCount(state, action: PayloadAction<number>) {
			state.count = action.payload
		},
		setTypes(state, action: PayloadAction<ServiceTypeState['types']>) {
			state.types = action.payload
		},
		filterTypes(state, action: PayloadAction<string>) {
			state.types = state.types.filter((s) =>
				stringIncludes(s.name, action.payload),
			)
		},
	},
	extraReducers: (builder) => {
		builder.addCase(fetchServiceTypes.pending, (state) => {
			state.isLoading = true
			state.isError = false
		})
		builder.addCase(fetchServiceTypes.fulfilled, (state, action) => {
			state.isLoading = false
			state.isError = false
			state.types = action.payload
			state.count = action.payload?.length || 0
		})
		builder.addCase(fetchServiceTypes.rejected, (state) => {
			state.isLoading = false
			state.isError = true
			state.types = []
			state.count = 0
		})
	},
})

export const serviceTypeReducer = serviceTypeSlice.reducer
export const serviceTypeSelectors = serviceTypeSlice.selectors
export const serviceTypeActions = serviceTypeSlice.actions
