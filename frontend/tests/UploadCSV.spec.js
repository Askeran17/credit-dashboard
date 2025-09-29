import { mount } from '@vue/test-utils'
import UploadCSV from '@/views/UploadCSV.vue'
import api from '@/services/api'
import { vi, describe, it, expect, beforeEach } from 'vitest'

vi.mock('@/services/api', () => ({
  default: {
    post: vi.fn().mockResolvedValue({ data: {} })
  }
}))

describe('UploadCSV.vue', () => {
  beforeEach(() => {
    window.localStorage.clear()
  })

  it('alerts when institution id missing or not matching saved one', async () => {
    window.localStorage.setItem('institution_id', 'abc123')
    const wrapper = mount(UploadCSV)

    // Spy on alert
    const alertSpy = vi.spyOn(window, 'alert').mockImplementation(() => {})

    await wrapper.find('button.btn-success').trigger('click')
    expect(alertSpy).toHaveBeenCalledWith('Institution ID is required')
    alertSpy.mockRestore()
  })

  it('uploads when id matches and file is present', async () => {
    window.localStorage.setItem('institution_id', 'abc123')
    const wrapper = mount(UploadCSV)

    // set institution id
    await wrapper.find('input.input').setValue('abc123')

    // mock file input
    const file = new File(['a,b\n1,2'], 'test.csv', { type: 'text/csv' })
    const input = wrapper.find('input[type="file"]')
    // set element value programmatically and trigger change
    Object.defineProperty(input.element, 'files', { value: [file] })
    await input.trigger('change')

    // Stub alert to silence and assert
    const alertSpy = vi.spyOn(window, 'alert').mockImplementation(() => {})

    await wrapper.find('button.btn-success').trigger('click')

    expect(api.post).toHaveBeenCalledWith('/loans/import/abc123', expect.any(FormData))
    expect(alertSpy).toHaveBeenCalledWith('CSV uploaded!')

    alertSpy.mockRestore()
  })
})
