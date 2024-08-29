import { IServiceType } from '@/models/service-type'

export interface IService {
	name: string
	price: string
	employee: number
	service_type: IServiceType
}

export interface ServiceState {
	count: number
	services: IService[]
}
