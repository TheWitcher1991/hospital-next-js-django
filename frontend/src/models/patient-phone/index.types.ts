export interface IBasePatientPhone {
	phone: string
}

export interface IPatientPhone extends IBasePatientPhone {
	id: number
}

export interface ICreatePatientPhone extends IBasePatientPhone {
	patient: number
}
