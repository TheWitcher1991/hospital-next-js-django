import { combineReducers, configureStore } from '@reduxjs/toolkit'
// import {setupListeners} from "@reduxjs/toolkit/query";
import { accountReducer } from '@/models/account'
import { AuthService } from '@/models/auth'

const RootReducer = combineReducers({
	account: accountReducer,
	[AuthService.reducerPath]: AuthService.reducer,
})

export const store = configureStore({
	reducer: RootReducer,
	middleware: (getDefaultMiddleware) =>
		getDefaultMiddleware().concat(AuthService.middleware),
})

export type AppStore = ReturnType<typeof store>
export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch

// setupListeners(store.dispatch)
