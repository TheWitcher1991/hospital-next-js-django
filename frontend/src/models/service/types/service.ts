import { IServiceType } from '@/models/service/types/service-type'

export interface IService {
	name: string
	price: string
	employee: number
	service_type: IServiceType
}
