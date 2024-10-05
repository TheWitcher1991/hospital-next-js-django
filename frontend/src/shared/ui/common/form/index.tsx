import { useEffect } from 'react'
import { Controller, useForm } from 'react-hook-form'
import type {
	FieldValues,
	ControllerProps,
	UseFormProps,
	UseFormSetValue,
} from 'react-hook-form'
import type { UseControllerProps } from 'react-hook-form/dist/types/controller'
import { Button, Label, LabelError } from '@shared/ui'

interface FieldType<T extends FieldValues>
	extends Pick<UseControllerProps<T>, 'name' | 'rules'> {
	label?: string
	render: ControllerProps<T>['render']
}

interface Props<T extends FieldValues> {
	fields: FieldType<T>[]
	title?: string
	onSubmit: (values: T) => void
	btnText: string
	config: UseFormProps<T>
	disabled?: boolean
	styleBtn?: string
	onResetButton?: boolean
	onResetSubmit?: boolean
	updateValueCallback?: (value: UseFormSetValue<T>) => void
}

function Form<T extends FieldValues>({
	fields,
	title,
	disabled,
	onSubmit,
	btnText,
	config,
	updateValueCallback,
	onResetButton = false,
	onResetSubmit = false,
}: Props<T>) {
	const {
		control,
		handleSubmit,
		formState: { errors },
		reset,
		setValue,
	} = useForm<T>(config)

	useEffect(() => {
		if (updateValueCallback) {
			updateValueCallback(setValue)
		}
	}, [updateValueCallback, setValue])

	const onResetSubmitAction = (data: T) => {
		onSubmit(data)
		onResetSubmit && reset()
	}

	return (
		<form onSubmit={handleSubmit(onResetSubmitAction)}>
			{title && <h4>{title}</h4>}
			<div>
				{fields.map(({ label, ...field }, index) => (
					<div key={`item-${index}`}>
						{label && <Label htmlFor={field.name}>{label}</Label>}
						<Controller<T> control={control} {...field} />
						{errors[field.name] && (
							<LabelError>
								{errors[field.name].message}
							</LabelError>
						)}
					</div>
				))}
			</div>
			<Button type='submit' disabled={disabled}>
				{btnText}
			</Button>
			{onResetButton && (
				<Button type='button' onClick={() => reset()}>
					сбросить
				</Button>
			)}
		</form>
	)
}

export default Form
