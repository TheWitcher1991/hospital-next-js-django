import { combineReducers } from '@reduxjs/toolkit'
import { accountReducer } from '@/models/account'
import { AuthApi } from '@/models/auth'
import { ServiceApi } from '@/models/service'
import { ServiceTypeApi, serviceTypeReducer } from '@/models/service-type'
import { serviceReducer } from '@/models/service'

export const RootReducer = combineReducers({
	account: accountReducer,
	service: serviceReducer,
	serviceType: serviceTypeReducer,
	[AuthApi.reducerPath]: AuthApi.reducer,
	[ServiceApi.reducerPath]: ServiceApi.reducer,
	[ServiceTypeApi.reducerPath]: ServiceTypeApi.reducer,
})
