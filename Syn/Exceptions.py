"""
Exception classes

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 6th, 2011, 01:50 -0000

 Lots of exceptions that we'll end up throwing later on in the
 Syn runtime.
"""

class SynException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class SynShittyPlumbingException(SynException):
	pass

class SynUnknownStatusException(SynException):
	pass

class SynDirectoryFailure(SynException):
	pass

class SynFormatException(SynException):
	pass

class ArchiveNotFoundException(SynException):
	pass

class InvalidJSONException(SynException):
	pass

class InvalidArchiveException(SynException):
	pass

class NotAnArchiveException(SynException):
	pass

class FileNotPresentException(SynException):
	pass

class BuildFailureException(SynException):
	pass

class MutexException(SynException):
	pass

class PackageNotFoundException(SynException):
	pass

class ConflictException(SynException):
	pass

class PackageInstalledException(SynException):
	pass

class PackageNotinstalledException(SynException):
	pass

class PackageUninstalledException(PackageNotinstalledException):
	pass

