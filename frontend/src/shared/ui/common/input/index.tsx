import { FC } from 'react'
import styles from './index.module.css'

export type InputProps = OmitClassName<DetailedInputProps>

export const Input: FC<InputProps> = ({ ...rest }) => {
	return <input className={styles.input} {...rest} />
}
