import { FC } from 'react'
import styles from './index.module.css'

interface SkeletonProps {
	variant?: 'rounded' | 'rectangular' | 'text' | 'ellipsis'
	width?: number
	height?: number
	maxHeight?: number
	maxWidth?: number
}

export const Skeleton: FC<SkeletonProps> = props => {
	const {
		variant = 'text',
		width = false,
		height = false,
		maxHeight,
		maxWidth,
		white,
	} = props

	let borderRadius = '4px'

	if (variant === 'rounded') {
		borderRadius = '50%'
	} else if (variant === 'rectangular') {
		borderRadius = '0.5rem'
	} else if (variant === 'ellipsis') {
		borderRadius = '20px'
	}

	return (
		<div
			className={`${styles.skeleton}`}
			style={{
				width: width ? `${width}px` : '100%',
				height: `${height}px`,
				maxHeight: `${maxHeight}px`,
				maxWidth: `${maxWidth}px`,
				borderRadius: borderRadius,
			}}
		/>
	)
}
