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
import { PatientTypeApi } from '@/models/patient-type'
import { PatientApi } from '@/models/patient'
import { PatientCartApi } from '@/models/patient-cart'
import { PatientPhoneApi } from '@/models/patient-phone'
import { PatientSignatureApi } from '@/models/patient-signature'
import { PatientBalanceApi } from '@/models/patient-balance'
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
	[PatientTypeApi.reducerPath]: PatientTypeApi.reducer,
	[PatientApi.reducerPath]: PatientApi.reducer,
	[PatientCartApi.reducerPath]: PatientCartApi.reducer,
	[PatientPhoneApi.reducerPath]: PatientPhoneApi.reducer,
	[PatientSignatureApi.reducerPath]: PatientSignatureApi.reducer,
	[PatientBalanceApi.reducerPath]: PatientBalanceApi.reducer,
	toastr: toastrReducer,
})
