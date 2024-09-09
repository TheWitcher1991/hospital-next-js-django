import { createAsyncThunk, GetThunkAPI } from '@reduxjs/toolkit'
import { AsyncThunkConfig } from '@reduxjs/toolkit/src/createAsyncThunk'
import { toastError } from '@/shared/utils'

interface CreateCoreAsyncThunkOptions<T> {
	typePrefix: string
	payloadCreator: (
		data: T,
		thunkApi: GetThunkAPI<AsyncThunkConfig>,
	) => Promise<T>
}

/**
 * @TODO: Доработать логику
 * @WARNING: Не используется
 */
export const coreAsyncThunk = <T, U>({
	typePrefix,
	payloadCreator,
}: CreateCoreAsyncThunkOptions<U>) => {
	return createAsyncThunk<T, U>(typePrefix, async (data: T, thunkApi) => {
		try {
			return payloadCreator(data, thunkApi)
		} catch (error) {
			toastError(error)
			return thunkApi.rejectWithValue(error)
		}
	})
}
