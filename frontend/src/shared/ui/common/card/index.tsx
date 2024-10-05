import { CSSProperties, FC } from 'react'
import styles from './index.module.css'

interface CardProps extends Omit<DetailedDivProps, 'className' | 'style'> {
	radius?: Size
	fullWidth?: boolean
	isHoverable?: boolean
	style?: CSSProperties
}

export const Card: FC<CardProps> = ({
	radius = 'sm',
	fullWidth,
	isHoverable,
	children,
	style,
	...rest
}) => {
	const radiusStyle = {
		sm: styles.card__radius__sm,
		md: styles.card__radius__md,
		lg: styles.card__radius__lg,
	}

	return (
		<div
			{...rest}
			style={style}
			className={`${styles.card} ${radiusStyle[radius]} ${fullWidth ? styles.card__full__width : ''} ${isHoverable ? styles.card__hoverable : ''}`}
		>
			{children}
		</div>
	)
}
