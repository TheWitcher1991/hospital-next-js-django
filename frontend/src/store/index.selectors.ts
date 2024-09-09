import { RootState } from '@/store/index.store'

export const AppSelectors = {
	getAuth: (state: RootState) => state.auth,
	getAccount: (state: RootState) => state.account,
	getServiceType: (state: RootState) => state.serviceType,
	getService: (state: RootState) => state.service,
}
