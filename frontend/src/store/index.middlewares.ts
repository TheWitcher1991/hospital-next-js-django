import { AuthApi } from '@/models/auth'
import { ServiceApi, ServiceTypeApi } from '@/models/service'

export const AppMiddlewares = [
	AuthApi.middleware,
	ServiceApi.middleware,
	ServiceTypeApi.middleware,
]
