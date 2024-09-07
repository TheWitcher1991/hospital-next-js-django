interface IBasePatientSignature {
	signature: string
}

export interface IPatientSignature extends IBasePatientSignature {
	id: number
}

export interface ICreatePatientSignature extends IBasePatientSignature {
	patient: number
}
