import { createAsyncThunk } from '@reduxjs/toolkit'
import { fetchCore } from '@/shared/libs'
import { ILogin, ILoginReturn } from '@/models/auth/index.types'
import { toastr } from 'react-redux-toastr'
import { ICreatePatient } from '@/models/patient'
import { ICreateEmployee } from '@/models/employee'
import { toastError } from '@/shared/utils'

export const signupPatient = createAsyncThunk<boolean, ICreatePatient>(
	'signup/patient',
	async (data, thunkApi) => {
		try {
			await fetchCore({
				url: 'v1/register/',
				method: 'POST',
				body: data,
			})
			toastr.success('Регистрация', 'Успешно выполнена')
			return true
		} catch (e) {
			toastError(e)
			return thunkApi.rejectWithValue(e)
		}
	},
)

export const signupEmployee = createAsyncThunk<boolean, ICreateEmployee>(
	'signup/employee',
	async (data, thunkApi) => {
		try {
			await fetchCore({
				url: 'v1/register/',
				method: 'POST',
				body: data,
			})
			toastr.success('Регистрация', 'Успешно выполнена')
			return true
		} catch (e) {
			toastError(e)
			return thunkApi.rejectWithValue(e)
		}
	},
)

export const login = createAsyncThunk<ILoginReturn, ILogin>(
	'auth/login',
	async ({ email, password }, thunkApi) => {
		try {
			const response = await fetchCore({
				url: 'v1/login/',
				method: 'POST',
			})
			toastr.success('Вход', 'Успешно выполнен')
			return (await response.json()) as ILoginReturn[]
		} catch (e) {
			toastError(e)
			return thunkApi.rejectWithValue(e)
		}
	},
)

export const logout = createAsyncThunk('auth/logout', async () => {
	return {}
})
