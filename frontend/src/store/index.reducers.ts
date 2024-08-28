import { combineReducers } from '@reduxjs/toolkit'
import { accountReducer } from '@/models/account'
import { AuthService } from '@/models/auth'

export const RootReducer = combineReducers({
	account: accountReducer,
	[AuthService.reducerPath]: AuthService.reducer,
})

export type RootState = ReturnType<typeof RootReducer>
