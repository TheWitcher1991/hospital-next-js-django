import { combineReducers } from '@reduxjs/toolkit'
import { accountReducer } from '@/models/account'
import { AuthApi } from '@/models/auth'
import { ServiceApi, ServiceTypeApi } from '@/models/service'

export const RootReducer = combineReducers({
	account: accountReducer,
	[AuthApi.reducerPath]: AuthApi.reducer,
	[ServiceApi.reducerPath]: ServiceApi.reducer,
	[ServiceTypeApi.reducerPath]: ServiceTypeApi.reducer,
})

export type RootState = ReturnType<typeof RootReducer>
