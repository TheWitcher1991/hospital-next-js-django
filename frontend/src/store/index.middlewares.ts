import { AuthApi } from '@/models/auth'
import { ServiceApi } from '@/models/service'
import { ServiceTypeApi } from '@/models/service-type'

export const AppMiddlewares = [
	AuthApi.middleware,
	ServiceApi.middleware,
	ServiceTypeApi.middleware,
]
