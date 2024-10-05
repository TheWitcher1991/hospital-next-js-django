import { FC } from 'react'
import styles from './index.module.css'

interface ButtonProps extends OmitClassName<DetailedButtonProps> {
	radius?: Size
	variant?: 'default' | 'primary' | 'secondary' | 'black' | 'danger'
}

export const Button: FC<ButtonProps> = ({
	radius = 'lg',
	variant = 'default',
	children,
	...rest
}) => {
	const variantStyle = {
		default: styles.button__default,
		primary: styles.button__primary,
		secondary: styles.button__secondary,
		black: styles.button__black,
		danger: styles.button__danger,
	}

	const radiusStyle = {
		sm: styles.button__radius__sm,
		md: styles.button__radius__md,
		lg: styles.button__radius__lg,
	}

	return (
		<button
			{...rest}
			className={`${styles.button} ${variantStyle[variant]} ${radiusStyle[radius]}`}
		>
			{children}
		</button>
	)
}
