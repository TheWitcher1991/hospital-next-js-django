import { IShift } from '@/models/shift'
import { IEmployee } from '@/models/employee'

export interface ISchedule {
	id: number
	date: string
	shift: IShift
	employee: IEmployee
}
