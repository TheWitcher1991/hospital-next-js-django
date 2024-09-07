import { PatientCartStatus } from '@/models/patient-cart/index.enums'
import { IPatient } from '@/models/patient'
import { IService } from '@/models/service'

export interface IBasePatientCart {
	diagnose: string
	date_visit: Nullable<string>
	status: PatientCartStatus
}

export interface IPatientCart extends IBasePatientCart {
	created: string
	patient: IPatient
	service: IService
}

export interface IUpdatePatientCart extends IBasePatientCart {
	patient: number
	service: number
}

export interface ICreatePatientCart extends IBasePatientCart {
	service: number
}
