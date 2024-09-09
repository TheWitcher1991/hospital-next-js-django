import { IPatientCart } from '@/models/patient-cart'

export interface IBaseAgreement {
	start: string
	end: string
}

export interface IAgreement extends IBaseAgreement {
	id: number
	patient_cart: IPatientCart
}

export interface ICreateAgreement extends IBaseAgreement {
	patient_cart: number
}

export type IUpdateAgreement = IBaseAgreement
