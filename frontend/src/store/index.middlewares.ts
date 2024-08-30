import { AuthApi } from '@/models/auth'
import { ServiceApi } from '@/models/service'
import { ServiceTypeApi } from '@/models/service-type'
import { Middleware, MiddlewareAPI } from 'redux'
import { isRejectedWithValue } from '@reduxjs/toolkit'

export const AppMiddlewares = [
	AuthApi.middleware,
	ServiceApi.middleware,
	ServiceTypeApi.middleware,
]

export const RTKQueryErrorLoggerMiddleware: Middleware =
	(api: MiddlewareAPI) => next => action => {
		if (isRejectedWithValue(action)) {
			console.error(action.error, 'RTK Query Error')
		}

		return next(action)
	}
