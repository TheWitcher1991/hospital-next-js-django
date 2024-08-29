import { FC, PropsWithChildren } from 'react'
import styles from './index.module.css'

interface ContainerProps extends PropsWithChildren {
	variant?: 'default' | 'small'
}

export const Container: FC<ContainerProps> = ({ children, variant }) => {
	let styleVariant = styles.container__default

	if (variant === 'small') styleVariant = styles.container__small

	return (
		<div className={`${styles.container} ${styleVariant} `}>{children}</div>
	)
}
