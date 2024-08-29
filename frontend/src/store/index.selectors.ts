import { RootState } from '@/store/index.reducers'

export const AppSelectors = {
	getAccount: (state: RootState) => state.account,
}
