import { combineReducers } from '@reduxjs/toolkit'
import { accountReducer } from '@/models/account'
import { AuthApi } from '@/models/auth'
import { ServiceApi } from '@/models/service'
import { ServiceTypeApi, serviceTypeReducer } from '@/models/service-type'
import { serviceReducer } from '@/models/service'
import { EmployeeApi } from '@/models/employee'
import { CabinetApi } from '@/models/cabinet'
import { PositionApi } from '@/models/position'
import { ShiftApi } from '@/models/shift'
import { ScheduleApi } from '@/models/schedule'
import { reducer as toastrReducer } from 'react-redux-toastr'

export const RootReducer = combineReducers({
	account: accountReducer,
	service: serviceReducer,
	serviceType: serviceTypeReducer,
	[AuthApi.reducerPath]: AuthApi.reducer,
	[ServiceApi.reducerPath]: ServiceApi.reducer,
	[ServiceTypeApi.reducerPath]: ServiceTypeApi.reducer,
	[EmployeeApi.reducerPath]: EmployeeApi.reducer,
	[CabinetApi.reducerPath]: CabinetApi.reducer,
	[PositionApi.reducerPath]: PositionApi.reducer,
	[ShiftApi.reducerPath]: ShiftApi.reducer,
	[ScheduleApi.reducerPath]: ScheduleApi.reducer,
	toastr: toastrReducer,
})
