import { useStore } from 'react-redux'
import { AppStore } from '@/store'

export const useAppStore = useStore.withTypes<AppStore>()
