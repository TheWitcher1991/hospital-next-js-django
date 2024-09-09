import { createSlice, PayloadAction } from '@reduxjs/toolkit'
import { AuthState } from './index.types'
import { login, logout, signupEmployee, signupPatient } from './index.thunks'

const initialState: AuthState = {
	isLoading: false,
}

export const authSlice = createSlice({
	name: 'auth',
	initialState,
	reducers: {
		setAuthIsLoading: (state, action: PayloadAction<boolean>) => {
			state.isLoading = action.payload
		},
	},
	extraReducers: builder => {
		builder.addCase(signupPatient.pending, state => {
			state.isLoading = true
		})
		builder.addCase(signupPatient.fulfilled, state => {
			state.isLoading = false
		})
		builder.addCase(signupPatient.rejected, state => {
			state.isLoading = false
		})
		builder.addCase(signupEmployee.pending, state => {
			state.isLoading = true
		})
		builder.addCase(signupEmployee.fulfilled, state => {
			state.isLoading = false
		})
		builder.addCase(signupEmployee.rejected, state => {
			state.isLoading = false
		})
		builder.addCase(login.pending, state => {
			state.isLoading = true
		})
		builder.addCase(login.fulfilled, state => {
			state.isLoading = false
		})
		builder.addCase(login.rejected, state => {
			state.isLoading = false
		})
		builder.addCase(logout.pending, state => {
			state.isLoading = true
		})
		builder.addCase(logout.fulfilled, state => {
			state.isLoading = false
		})
		builder.addCase(logout.rejected, state => {
			state.isLoading = false
		})
	},
})

export const authReducer = authSlice.reducer
export const authSelectors = authSlice.selectors
export const authActions = authSlice.actions
