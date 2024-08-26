import { AccountState } from '@/models/account/types'
import { createSlice, PayloadAction } from '@reduxjs/toolkit'
import {
	loadStateFromLocalStorage,
	saveStateToLocalStorage,
} from '@/models/account/storage'

const initialState: Nullable<Partial<AccountState>> =
	loadStateFromLocalStorage()

export const accountSlice = createSlice({
	name: 'account',
	initialState,
	reducers: {
		login: (state, action: PayloadAction<AccountState>) => {
			Object.assign(state, action.payload)
			saveStateToLocalStorage(state)
		},
		logout: (state) => {
			Object.assign(state, initialState)
			saveStateToLocalStorage(state)
		},
	},
})

export const accountReducer = accountSlice.reducer
export const accountActions = accountSlice.actions
