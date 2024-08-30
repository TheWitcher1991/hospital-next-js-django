import { createSlice, PayloadAction } from '@reduxjs/toolkit'
import { AccountState } from '@/models/account/index.types'

const initialState: Nullable<Partial<AccountState>> = {
	isAuthenticated: false,
}

export const accountSlice = createSlice({
	name: 'account',
	initialState,
	reducers: {
		login(state, action: PayloadAction<AccountState>) {
			Object.assign(state, action.payload)
		},
		logout(state) {
			Object.assign(state, initialState)
		},
	},
})

export const accountReducer = accountSlice.reducer
export const accountSelectors = accountSlice.selectors
export const accountActions = accountSlice.actions
