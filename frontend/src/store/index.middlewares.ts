import { Middleware, MiddlewareAPI } from 'redux'
import { isRejectedWithValue } from '@reduxjs/toolkit'
import { AuthApi } from '@/models/auth'
import { ServiceApi } from '@/models/service'
import { ServiceTypeApi } from '@/models/service-type'
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
import { AgreementApi } from '@/models/agreement'
import { TalonApi } from '@/models/talon'

export const AppMiddlewares = [
	AuthApi.middleware,
	ServiceApi.middleware,
	ServiceTypeApi.middleware,
	EmployeeApi.middleware,
	CabinetApi.middleware,
	PositionApi.middleware,
	ShiftApi.middleware,
	ScheduleApi.middleware,
	PatientTypeApi.middleware,
	PatientApi.middleware,
	PatientCartApi.middleware,
	PatientPhoneApi.middleware,
	PatientSignatureApi.middleware,
	PatientBalanceApi.middleware,
	AgreementApi.middleware,
	TalonApi.middleware,
]

export const RTKQueryErrorLoggerMiddleware: Middleware =
	(api: MiddlewareAPI) => next => action => {
		if (isRejectedWithValue(action)) {
			console.error(action.error, 'RTK Query Error')
		}

		return next(action)
	}
